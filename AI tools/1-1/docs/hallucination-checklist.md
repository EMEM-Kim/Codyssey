# 5개 환각 검증 원문 질문과 코드 근거 — 평가 #5, #12

**평가 대상:** 기존 STEP 4의 원문 질의와 AI 원문 발췌. 각 질문에 대한 'A'는 제공된 코드와 답변의 핵심이 일치한다는 **문서 작성자 재평가**이며, 독립된 평가자 최종 판정은 아니다.

| 번호 | 원문 질문 | 기대 사실·코드 근거 | 관찰 응답 핵심 | 판정 |
|---|---|---|---|---|
| 1 | "PR Guardian, 방금 리뷰한 UserProfileView의 permission_classes에는 정확히 어떤 권한 클래스가 설정되어 있어? 제공된 코드에서 근거를 함께 제시해 줘." | `permission_classes = [AllowAny]` | AllowAny | A |
| 2 | "PR Guardian, 방금 리뷰한 UserProfileView의 GET 메서드가 응답으로 반환하는 사용자 정보는 정확히 어떤 필드들이야? 제공된 코드에서 근거를 함께 제시해 줘." | `Response({"id": user.id, "username": user.username, "email": user.email})` | id, username, email | A |
| 3 | "PR Guardian, 방금 리뷰한 UserProfileView의 PATCH 메서드에서 입력받은 nickname 값은 실제로 User 모델의 어떤 필드에 저장돼? 해당 코드와 근거를 함께 설명해 줘." | `user.username = nickname` | username | A |
| 4 | "PR Guardian, 현재 UserProfileView의 PATCH 메서드에는 닉네임이 2~20자인지 검증하는 로직이 구현되어 있어? 코드에 근거해 답변해 줘." | `nickname = request.data.get("nickname")` 후 `user.username = nickname`; 길이 비교·Serializer 없음 | 검증 없음 | A |
| 5 | "PR Guardian, 현재 UserProfileView에서 존재하지 않는 user_id로 GET 또는 PATCH 요청이 들어왔을 때 User.DoesNotExist 예외를 처리하는 로직이 구현되어 있어? 제공된 코드에 근거해 설명해 줘." | `User.objects.get(id=user_id)` 호출, 뷰 내 `try/except` 없음 | 처리 없음 | A |

**유의:** 코드에 예외 처리가 없다는 사실은 확인 가능하지만 실제 운영 환경의 최종 HTTP 상태 코드는 별도 전역 처리기에 따라 달라질 수 있다. AI 응답 전문은 `run-log.md`에서 일부만 보존됨.
