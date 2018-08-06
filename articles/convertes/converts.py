class FourDigitYearConverter:
    # 定义匹配规则
    regex = '[0-9]{4}'

    # 参数的转换
    def to_python(self, value):
        return int(value)

    # url配置
    def to_url(self, value):
        return '%04d' % value
