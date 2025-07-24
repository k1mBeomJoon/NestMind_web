from django.contrib.auth.models import User
from accounts.models import Profile

def migrate_nicknames():
    count = 0
    skipped = 0
    for user in User.objects.all():
        if user.first_name:
            # 이미 닉네임이 존재하면 건너뜀
            if Profile.objects.filter(nickname=user.first_name).exists():
                print(f"[SKIP] {user.username}: 닉네임 '{user.first_name}' 중복")
                skipped += 1
                continue
            profile = getattr(user, 'profile', None)
            if profile:
                profile.nickname = user.first_name
                profile.save()
                print(f"[OK] {user.username}: '{user.first_name}' → Profile.nickname")
                count += 1
    print(f"총 {count}명 닉네임 이전 완료, {skipped}명 중복으로 건너뜀.")

if __name__ == "__main__":
    migrate_nicknames() 