# Few-shot 입력·기대 응답 예시 3건 — 평가 #4

> 다음은 프롬프트 설계에 사용한 **예시 입력과 기대 출력**이다. 실제 모델에 각각 별도 질의하여 얻은 대화 로그라고 주장하지 않는다. Zero-shot/Few-shot 비교에서는 이 3개 예시를 포함한 프롬프트를 사용했다.

## 예시 1: 인증·인가 누락
**입력 원문**
```text
요구사항: 관리자만 데이터를 삭제할 수 있다.
class AdminView(APIView):
    permission_classes = [AllowAny]

    def delete(self, request, item_id):
        Item.objects.filter(id=item_id).delete()
        return Response({"message": "삭제 완료"})
```
**기대 응답 예시**
```text
문제 #1 — Critical
위치: AdminView.permission_classes 및 delete()
근거: AllowAny와 관리자 권한 검사 부재
영향: 인증되지 않은 사용자에게 삭제 기능이 노출될 수 있음
개선: IsAuthenticated와 관리자 권한 확인 추가
최종 의견: Request Changes
```

## 예시 2: 입력 검증 누락
**입력 원문**
```text
요구사항: 주문 수량은 1~100이다.
def post(self, request):
    quantity = request.data.get("quantity")
    order = Order.objects.create(quantity=quantity)
    return Response({"id": order.id})
```
**기대 응답 예시**
```text
문제 #1 — High
위치: post()
근거: quantity를 검증 없이 저장에 사용
영향: 허용 범위 밖의 값이 저장되거나 오류 발생 가능
개선: Serializer에서 정수형 및 1~100 범위 검증
최종 의견: Request Changes
```

## 예시 3: 정보 부족 시 되묻기
**입력 원문**
```text
로그인 기능에 문제가 있는 것 같아. 코드 리뷰해 줘.
```
**기대 응답 예시**
```text
제공된 코드가 없어 실제 원인을 단정할 수 없습니다.
1. 로그인 관련 View/Serializer 코드를 보여줄 수 있나요?
2. 어떤 오류 메시지나 재현 증상이 있나요?
3. JWT, 세션 등 어떤 인증 방식을 사용하나요?
코드를 받으면 확인 가능한 부분부터 리뷰하겠습니다.
```

## 실제 실행과 구분
- 위 3건은 **프롬프트 내 시범 예시**이다.
- 실제 Zero-shot/Few-shot 응답 비교는 `zero-vs-few-shot.md` 참조.
- 개별 예시를 별도 모델에 입력한 결과 원문은 확보되지 않았으므로 '실제 대화 3건'으로 계산하지 않는다.
