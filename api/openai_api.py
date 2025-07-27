import base64
from openai import OpenAI
from utils.config import OPENAI_API_KEY
from utils.file_handler import encode_image_to_base64
import re
import json

client = OpenAI(api_key=OPENAI_API_KEY)

def request_info_description(image_path, prompt):
    try:
        with open(image_path, "rb") as f:
            image_data = f.read()
        base64_image = base64.b64encode(image_data).decode("utf-8")

        response = client.chat.completions.create(
            model="gpt-4o",
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
            max_tokens=300
        )

        return response.choices[0].message.content
    except Exception as e:
        return f"api 호출 오류 : {str(e)}"


def generate_description(self):
    if not self.image_path:
        self.result_output.setPlainText("이미지를 먼저 불러와 주세요.")
        return

    prompt = f"""
                이 이미지는 가상의 인물 캐릭터입니다.
                관상 전문가로서, 동양 관상학적인 기준에 따라 이 인물의 성향을 분석해주세요.
                재미로 보려고 하는거니까 너무 정확할 필요없이 적당하게 분석해주세요.
                조금 더 길게 전문가처럼 분석해주세요.

                다음 항목을 포함해서 JSON 형식으로 분석해 주세요:

                1. 재물운
                2. 연애운
                3. 건강운
                4. 전체 요약 (200자 이내)

                {{
                "money": "...",
                "love": "...",
                "health": "...",
                "summary": "..."
                }}
                """

    try:
        base64_image = encode_image_to_base64(self.image_path)
        result = request_info_description(self.image_path, prompt)

        matched_data = re.search(r'```json\s*(\{.*?\})\s*```', result, re.DOTALL)
        if matched_data:
            json_str = matched_data.group(1)
            parsed_data = json.loads(json_str)
            self.money_contents.setText(parsed_data["money"])
            self.love_contents.setText(parsed_data["love"])
            self.health_contents.setText(parsed_data["health"])
            self.summary_contents.setText(parsed_data["summary"])

        # with sqlite3.connect(DB_PATH) as conn:
        #     cursor = conn.cursor()
        #     with open(self.image_path, "rb") as f:
        #         image_blob = f.read()
        #     cursor.execute('''
        #         INSERT INTO image_logs (image, prompt, response) VALUES (?, ?, ?)
        #     ''', (image_blob, prompt, result))
        #     conn.commit()

    except Exception as e:
        self.result_output.setPlainText(f"응답 오류 발생: {e}")