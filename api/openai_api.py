import base64
from openai import OpenAI
from utils.config import OPENAI_API_KEY
from utils.file_handler import encode_image_to_base64

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
            max_tokens=300
        )

        return response.choices[0].message.content
    except Exception as e:
        return f"api 호출 오류 : {str(e)}"


def generate_description(self):
    if not self.image_path or not self.link_address_text:
        self.result_output.setPlainText("이미지를 먼저 불러와 주세요.")
        return

    prompt = f"""
                {self.link_address_text} 혹은
                {self.image_path} 이미지에 대해서
                평점 정보, 대표 메뉴 이미지, 가장 추천이 많은 리뷰, 위치 정보에 대한 정보를
                만약 링크가 있을 경우 그 해당 링크의 도메인(네이버지도 혹은 카카오맵)에서
                데이터를 추출해서 알려줘
                """

    try:
        base64_image = encode_image_to_base64(self.image_path)
        result = request_info_description(self.image_path, prompt)
        self.result_output.setPlainText(result)

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