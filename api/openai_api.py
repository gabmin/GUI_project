import base64
from PyQt5.QtWidgets import QMessageBox
from openai import OpenAI
from utils.config import OPENAI_API_KEY
from utils.file_handler import encode_image_to_base64
import re
import json
import sqlite3
from utils.config import DB_PATH

client = OpenAI(api_key=OPENAI_API_KEY)

def request_info_description(image_path, prompt):
    try:
        with open(image_path, "rb") as f:
            image_data = f.read()
        base64_image = base64.b64encode(image_data).decode("utf-8")

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            }
                        }
                    ]
                }
            ],
            max_tokens=3000
        )

        return response.choices[0].message.content
    except Exception as e:
        return f"api 호출 오류 : {str(e)}"


def generate_description(self):
    if not self.image_path:
        QMessageBox.warning(self, "오류", "이미지를 등록해주세요!!")
        return

    prompt = f"""
                당신은 요리 전문가입니다.

                {self.image_path}를 분석해서 재료를 파악하고,

                다음 재료를 사용하여 만들 수 있는 요리 레시피 1개를 JSON 형식으로 제시해주세요.

                형식은 다음과 같이 맞춰주세요:

                {{
                "ingredients_name": "재료명",
                "recipe": {{
                    "name": "요리 이름",
                    "ingredients": ["재료1", "재료2", "..."],
                    "steps": [
                    "1단계 설명",
                    "2단계 설명",
                    "3단계 설명"
                    ]
                }}
                }}

                요리법은 3000토큰 한도 내에서 최대한 자세하게 설명해주세요.
                응답은 순수 JSON 형식으로만 출력해 주세요. 백틱(```)이나 기타 마크다운 문법 없이 출력해 주세요.
            """

    try:
        result = request_info_description(self.image_path, prompt)

        if result:
            data = json.loads(result)
            print(type(data), data)
            ingredient = data.get("ingredients_name", "알 수 없음")
            recipe = data.get("recipe", [])

            formatted = f"<b>재료:</b> {ingredient}<br><br>"

            formatted += f"<b>1. {recipe.get('name', '알 수 없는 요리')}</b><br>"
            formatted += f"<u>재료:</u> {', '.join(recipe.get('ingredients', []))}<br>"
            formatted += "<u>요리법:</u><br>"
            for step_num, step in enumerate(recipe.get('steps', []), 1):
                formatted += f"&nbsp;&nbsp;{step_num}. {step}<br>"

            self.result_label.setText(formatted)
        else:
            QMessageBox.warning(self, "오류", "이미지를 이해하지 못했습니다. 다른 이미지를 등록해주세요.")
            return

        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            with open(self.image_path, "rb") as f:
                image_blob = f.read()
            cursor.execute('''
                INSERT INTO recipe_logs (ingredients_name, image, recipe_description) VALUES (?, ?, ?)
            ''', (ingredient, image_blob, formatted))
            conn.commit()

    except Exception as e:
        print(e)
        QMessageBox.warning(self, "오류", "오류가 발생했습니다. 다시 시도해주세요.")