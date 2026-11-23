import ast
import unittest

SOURCE = '''from rest_framework.views import APIView
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
'''

class ReviewAssertions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tree = ast.parse(SOURCE)
        cls.view = next(n for n in cls.tree.body if isinstance(n, ast.ClassDef) and n.name == 'UserProfileView')
        cls.methods = {n.name:n for n in cls.view.body if isinstance(n, ast.FunctionDef)}

    def test_allow_any(self):
        assignment = next(n for n in self.view.body if isinstance(n, ast.Assign) and any(isinstance(t,ast.Name) and t.id=='permission_classes' for t in n.targets))
        self.assertEqual([e.id for e in assignment.value.elts], ['AllowAny'])

    def test_get_fields(self):
        d = next(n for n in ast.walk(self.methods['get']) if isinstance(n, ast.Dict))
        self.assertEqual([k.value for k in d.keys], ['id','username','email'])

    def test_patch_writes_username(self):
        self.assertTrue(any(isinstance(n,ast.Assign) and any(isinstance(t,ast.Attribute) and t.attr=='username' for t in n.targets) for n in ast.walk(self.methods['patch'])))

    def test_no_length_validation(self):
        self.assertFalse(any(isinstance(n,ast.Compare) for n in ast.walk(self.methods['patch'])))
        self.assertNotIn('Serializer', SOURCE)

    def test_no_local_exception_handler(self):
        self.assertFalse(any(isinstance(n,ast.Try) for n in ast.walk(self.view)))

    def test_no_owner_check(self):
        self.assertNotIn('request.user', SOURCE)

    def test_updated_policy_boundaries(self):
        valid = lambda s: 3 <= len(s) <= 15
        self.assertFalse(valid('ab'))
        self.assertTrue(valid('abc'))
        self.assertTrue(valid('a'*15))
        self.assertFalse(valid('a'*16))

if __name__ == '__main__':
    unittest.main(verbosity=2)
