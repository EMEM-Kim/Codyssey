# STEP 4 — 실제 18턴 대화 기록

> **원문 보존 상태: 부분 전사.** 아래 User 메시지는 실제 원문이며 AI 메시지는 확인된 원문 **발췌**다. 생략된 AI 전문을 임의로 만들어 넣지 않는다. 사용자 9턴 + AI 9턴 = 18턴. 코드 실행은 수행하지 않았다.

## 실험 코드
```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User

class UserProfileView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        return Response({"id": user.id, "username": user.username, "email": user.email})

    def patch(self, request, user_id):
        user = User.objects.get(id=user_id)
        nickname = request.data.get("nickname")
        user.username = nickname
        user.save()
        return Response({"message": "프로필 수정 완료", "nickname": user.username})
```

## 발화별 기록
### Turn 1 — User (원문)
PR Guardian, 다음 GitHub PR을 리뷰해 줘.

PR 제목: 사용자 프로필 조회 및 수정 API 추가
개발 환경: Python 3.12 / Django 5 / Django REST Framework
요구사항: 로그인한 사용자는 자신의 프로필만 조회·수정할 수 있고, 닉네임은 2~20자여야 해.

변경 코드: 위 '실험 코드'와 동일.

STEP 3의 PR Guardian v1 규칙과 Few-shot 예시를 적용해 정해진 리뷰 형식으로 답변해 줘. 이 메시지부터 실제 실험 로그를 시작하고 사용자 및 AI 발화를 원문 그대로 보존해 줘.

### Turn 2 — AI (원문 발췌)
> 해당 PR은 사용자 프로필 조회(GET) 및 닉네임 수정(PATCH) 기능을 구현하고 있지만, 인증 및 사용자 소유권 검증이 누락되어 타인의 개인정보 조회와 계정 정보 변경이 가능합니다. 또한 닉네임 길이 검증과 존재하지 않는 사용자에 대한 예외 처리가 없어 요구사항을 충족하지 못합니다. 보안 취약점과 데이터 무결성 문제가 확인되므로 수정 후 재검토가 필요합니다.

문제 6개: 인증, 소유권, 닉네임 길이, username/nickname 혼용, 조회 예외, 고유성. 최종 **Request Changes**.

### Turn 3 — User (원문)
PR Guardian, 방금 리뷰한 UserProfileView의 permission_classes에는 정확히 어떤 권한 클래스가 설정되어 있어? 제공된 코드에서 근거를 함께 제시해 줘.

### Turn 4 — AI (원문 발췌)
> **답변:** `AllowAny` 권한 클래스가 설정되어 있습니다.

**예비 Pass** — 코드와 일치.

### Turn 5 — User (원문)
PR Guardian, 방금 리뷰한 UserProfileView의 GET 메서드가 응답으로 반환하는 사용자 정보는 정확히 어떤 필드들이야? 제공된 코드에서 근거를 함께 제시해 줘.

### Turn 6 — AI (원문 발췌)
> **답변:** GET 메서드는 총 **3개의 필드**를 반환합니다.
> 따라서 **GET 메서드의 응답 데이터 필드는 `id`, `username`, `email` 총 3개**입니다.

**예비 Pass** — 코드와 일치.

### Turn 7 — User (원문)
PR Guardian, 방금 리뷰한 UserProfileView의 PATCH 메서드에서 입력받은 nickname 값은 실제로 User 모델의 어떤 필드에 저장돼? 해당 코드와 근거를 함께 설명해 줘.

### Turn 8 — AI (원문 발췌)
> **답변:** 입력받은 `nickname` 값은 Django 기본 `User` 모델의 **`username` 필드**에 저장됩니다.

**예비 Pass** — `user.username = nickname`.

### Turn 9 — User (원문)
PR Guardian, 현재 UserProfileView의 PATCH 메서드에는 닉네임이 2~20자인지 검증하는 로직이 구현되어 있어? 코드에 근거해 답변해 줘.

### Turn 10 — AI (원문 발췌)
> **답변: 아니요. 닉네임 길이를 검증하는 로직은 구현되어 있지 않습니다.**

**예비 Pass** — 길이 검증 없음.

### Turn 11 — User (원문)
PR Guardian, 현재 UserProfileView에서 존재하지 않는 user_id로 GET 또는 PATCH 요청이 들어왔을 때 User.DoesNotExist 예외를 처리하는 로직이 구현되어 있어? 제공된 코드에 근거해 설명해 줘.

### Turn 12 — AI (원문 발췌)
> **답변: 아니요. 현재 코드에는 `User.DoesNotExist` 예외를 처리하는 로직이 구현되어 있지 않습니다.**

**예비 Pass** — 뷰 내부에 예외 처리 없음.

### Turn 13 — User (원문)
PR Guardian, 지금부터 프로젝트 요구사항이 변경됐어. 닉네임 허용 길이를 기존 2~20자에서 3~15자로 변경할게. 인증된 사용자만 자신의 프로필을 조회·수정할 수 있다는 조건은 그대로 유지해. 이 변경 사항을 반영해서 기존 PR을 다시 리뷰하고, 이전 리뷰와 비교해 어떤 판단이 달라지는지 설명해 줘.

### Turn 14 — AI (원문 발췌)
> 프로젝트의 닉네임 허용 길이가 기존 **2~20자에서 3~15자로 변경**되었습니다. 기존 `UserProfileView`에는 닉네임 길이 검증이 전혀 구현되어 있지 않으므로 변경된 요구사항도 충족하지 못합니다. 또한 인증 누락과 사용자 소유권 검증 누락 등 기존 보안 문제는 그대로 남아 있어 PR 수정이 필요합니다.

**예비 Pass** — 변경 조건과 유지 조건 모두 반영.

### Turn 15 — User (원문)
PR Guardian, 현재 프로젝트의 닉네임 길이 요구사항은 무엇이며, 기존 UserProfileView가 해당 요구사항을 충족하는지 설명해 줘.

### Turn 16 — AI (원문 발췌)
> 현재 프로젝트의 닉네임 허용 길이는 **3~15자**입니다.
> **충족하지 못합니다.**
> **최종 의견: Request Changes**

### Turn 17 — User (원문; Turn 15와 동일)
PR Guardian, 현재 프로젝트의 닉네임 길이 요구사항은 무엇이며, 기존 UserProfileView가 해당 요구사항을 충족하는지 설명해 줘.

### Turn 18 — AI (원문 발췌)
> 현재 프로젝트의 닉네임 허용 길이는 **3~15자**입니다.
> **기존 `UserProfileView`는 변경된 요구사항을 충족하지 못합니다.**
> **최종 의견: Request Changes**

## 판정
| 항목 | 결과 | 근거 |
|---|---|---|
| Q1 권한 클래스 | 예비 Pass | AllowAny |
| Q2 GET 응답 | 예비 Pass | id, username, email |
| Q3 PATCH 저장 필드 | 예비 Pass | username |
| Q4 길이 검증 | 예비 Pass | 없음 |
| Q5 DoesNotExist | 예비 Pass | 뷰 내부 처리 없음 |
| 조건 변경 | 예비 Pass | 3~15자 적용 |
| 동일 입력 2회 | 예비 Pass | 핵심 판단 일치 |

관찰된 명백한 환각이나 실패는 없다. 사용자 최종 Pass/Fail 판정은 미확정.

## 재현·제출 한계
- AI 응답은 전문이 아닌 원문 발췌다. **전체 원문 보존 요건은 아직 충족하지 않는다.**
- v1과 Few-shot은 별도의 실제 시스템 메시지 설치가 아닌 대화 내 지침이다.
- 실행 환경에서 API 테스트를 수행한 결과는 없다.
- 전체 전사 시 기존 발췌를 변경하지 말고 원문 전문을 대화 내보내기에서 추가한다.
