# STEP 2 — LLM 3종 비교

## 과업 및 비교 조건
- 과업: Python 3.12 / Django 5 / DRF 기반 GitHub PR 정적 코드 리뷰
- 비교 모델: ChatGPT (GPT-6), Claude (사용자 기록: Sonnet 5.5 medium, 무료), Gemini (무료)
- 평가 기준: 버그 탐지 정확성, 사실성, 형식 준수, 수정안 실용성, 불확실성 처리 (각 5점)
- 공통 코드: `UserProfileView`에서 `AllowAny`, ID 소유권 미검증, 닉네임 길이 미검증, `username` 변경, `DoesNotExist` 미처리, 고유성 충돌 가능성
- 초기 요구사항: 인증된 사용자만 자신의 프로필 조회·수정, 닉네임 2~20자

## 비교 결과 (당시 평가 기록)
| 모델 | 버그 탐지 | 사실성 | 형식 | 실용성 | 불확실성 | 합계 |
|---|---:|---:|---:|---:|---:|---:|
| ChatGPT (GPT-6) | 5 | 5 | 5 | 4 | 5 | **24/25** |
| Claude | 5 | 4 | 4 | 5 | 5 | **23/25** |
| Gemini | 4 | 5 | 5 | 4 | 5 | **23/25** |

## 선택
ChatGPT를 후속 STEP 3~4의 실험 모델로 선정했다. 코드에 직접 나타난 문제와 실행 환경에 따라 달라질 수 있는 결과를 구분한 점이 선정 근거다.

## 추가 비교 실험 (완료)
- 사용자 제공 실제 응답을 바탕으로 Zero-shot **24/25**, Few-shot **23/25**로 평가했다. 각각 1회 수행했으며 일반화할 수 없다.
- 상세 비교와 실제 원문 발췌: [zero-vs-few-shot.md](zero-vs-few-shot.md)
- 초기 3모델 비교의 Claude·Gemini 원문 전문은 현재 저장소 문서에서 확인되지 않으므로, 점수별 직접 인용을 임의로 만들지 않는다. 원본 `테스트.txt`를 확보해 점수별 증거를 보완해야 한다.
- 입력 양식: [input-template.md](input-template.md), Few-shot 예시: [few-shot-transcripts.md](few-shot-transcripts.md).
