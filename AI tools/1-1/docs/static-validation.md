# 추가 실험 — 정적 코드 검증 (실제 실행)

## 실행 정보
- 방법: Python 표준 라이브러리 `ast` 및 `unittest`
- 대상: STEP 4에 사용된 `UserProfileView` 코드 문자열
- 실행: `python pr_review_checks.py`
- 결과: **7 tests, 7 passed**
- 주의: Django 서버나 DRF API를 실행한 것이 아니며, LLM Zero-shot/Few-shot A/B 실험도 아니다.

## 실제 결과
```text
test_allow_any ... ok
test_get_fields ... ok
test_no_length_validation ... ok
test_no_local_exception_handler ... ok
test_no_owner_check ... ok
test_patch_writes_username ... ok
test_updated_policy_boundaries ... ok

Ran 7 tests in 0.002s
OK
```

## 해석
1. `permission_classes = [AllowAny]` 존재를 확인했다.
2. GET의 반환 필드가 `id`, `username`, `email`임을 확인했다.
3. PATCH가 `user.username`을 변경함을 확인했다.
4. PATCH 내부 길이 비교 및 Serializer가 없음을 확인했다.
5. 뷰 내부의 `try/except`가 없음을 확인했다.
6. `request.user` 기반 소유권 검사가 없음을 확인했다.
7. **3~15자** 정책의 2/3/15/16자 경계 기대값을 확인했다.

## 한계
테스트는 소스 구조 및 정책의 경계값을 검증한다. 실제 API 동작, 데이터베이스 고유성 충돌, 인증 미들웨어, HTTP 응답 코드를 검증하지 않는다. 테스트 자체는 LLM 모델 응답 품질을 증명하지 않는다.
