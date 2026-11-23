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

## 기법별 적용 조건과 한계
| 기법 | 적용 조건 | 확인 가능한 것 | 확인 불가능한 것 |
|---|---|---|---|
| AST 구조 검사 | 유효한 Python 구문 | 명시된 클래스·속성·대입·분기 구조 | 런타임 미들웨어·동적 동작 |
| unittest | 독립된 검증 코드와 기대값 | 코드 구조에 대한 단언 성공 여부 | 실제 DRF 요청/DB 상태 |
| LLM 정적 리뷰 | 코드와 요구사항 제공 | 잠재적 취약점과 개선 제안 | 실제 공격 성공 여부, 운영 환경의 HTTP 상태 |

정적 검증에서 '7/7 통과'는 **취약점이 없다는 뜻이 아니라 기존 문제의 구조를 검증하는 테스트가 통과했다는 뜻**이다.
