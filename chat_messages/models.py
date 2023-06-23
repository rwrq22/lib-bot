from django.db import models
from common.models import CommonModel

### nltk로 키워드 추출###
""" import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer """

### openai ###
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


class Message(CommonModel):
    text = models.TextField()
    response = models.TextField(
        default="",
    )

    ########### 답변 생성 함수(openai 버전) ############
    def generate_response(self):
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a Hongik University library chatbot",
                },
                {
                    "role": "user",
                    "content": f"{self.text}",
                },
            ],
        )
        return completion["choices"][0]["message"]["content"]

    ########### 답변 생성 함수(NLTK 버전) ############
    """ def generate_response(self):
        sentence = self.text
        # 문장을 소문자로 변환
        sentence = sentence.lower()

        # 문장을 단어로 토큰화
        tokens = word_tokenize(sentence)

        # 불용어 제거
        stop_words = set(stopwords.words("english"))
        tokens = [token for token in tokens if token not in stop_words]

        # 단어의 형태소를 기본 형태로 변환 (lemmatization)
        lemmatizer = WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(token) for token in tokens]

        # 토큰화된 문장에서 명사만 추출
        tagged_tokens = nltk.pos_tag(tokens)
        keywords = [token for token, pos in tagged_tokens if pos.startswith("N")]

        return keywords """

    def save(self, *args, **kwargs):
        if not self.pk:
            self.response = self.generate_response()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return "Messages"


### 사용 안함
class ChatResponse(CommonModel):
    text = models.TextField()

    def __str__(self) -> str:
        return "Responses"
