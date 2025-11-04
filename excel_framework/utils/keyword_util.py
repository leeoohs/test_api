from faker import Faker


fk = Faker(locale='zh_CN')


def get_name():
    """生成中文名"""
    return fk.name()


def get_phone():
    """生成手机号"""
    return fk.phone_number()


if __name__ == '__main__':
    print(get_name())
    print(get_phone())
    print(fk.email())
    print(fk.address())
    print(fk.company())
    print(fk.job())
    print(fk.date())
    print(fk.date_time())