# 재사용 가능한 PR 리뷰 입력 템플릿 — 평가 #2

## 입력 형식: JSON (복사하여 값만 수정)
아래 JSON을 사용자 메시지에 붙여 넣고 코드 리뷰를 요청한다. `requirements`는 현재 유효한 조건만 기록한다. 코드의 줄바꿈은 JSON에서 `\n`으로 표시한다.

```json
{
  "task": "review_pull_request",
  "pr_title": "사용자 프로필 조회 및 수정 API 추가",
  "environment": {"python": "3.12", "django": "5", "framework": "DRF"},
  "requirements": [
    "인증된 사용자만 조회 및 수정 가능",
    "자신의 프로필만 조회 및 수정 가능",
    "닉네임 길이 2~20자"
  ],
  "files": [
    {
      "path": "views.py",
      "language": "python",
      "code": "class UserProfileView(APIView):\n    permission_classes = [AllowAny]\n    ..."
    }
  ],
  "review_focus": ["authentication", "authorization", "validation", "exception_handling"],
  "output_format": ["summary", "findings", "questions", "decision"]
}
```

**사용자 프롬프트:** "PR Guardian, 다음 JSON을 입력 명세로 사용해 리뷰해 줘. 실제 코드가 아닌 생략 기호(...)는 리뷰 대상으로 사용하지 마."

## 필드 규칙
| 필드 | 형식 | 필수 | 의미 |
|---|---|---|---|
| task | string | 예 | 작업 종류 |
| pr_title | string | 예 | PR 제목 |
| environment | object | 예 | 실행 환경 정보 |
| requirements | string[] | 예 | 현재 적용할 요구사항 |
| files | object[] | 예 | 경로, 언어, **전체 코드** |
| review_focus | string[] | 아니오 | 우선 검토 범위 |
| output_format | string[] | 예 | 결과 구조 |

## 응답 템플릿
```text
1. 전체 리뷰 요약
2. 발견된 문제
   #1 [Critical/High/Medium/Low]
   위치:
   문제:
   근거:
   영향:
   개선:
3. 추가 확인 사항 (최대 3개)
4. 최종 의견: Approve / Request Changes / Comment
```

이 템플릿은 **재사용을 위해 새로 작성한 예시**이며 기존 STEP 4의 실제 입력 원문은 아니다.
