from django.contrib.auth.password_validation import MinimumLengthValidator, NumericPasswordValidator,CommonPasswordValidator,UserAttributeSimilarityValidator, ValidationError, ngettext
from django.utils.translation import gettext_lazy as _


class MinimumLengthValidator(MinimumLengthValidator):
    
    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                ngettext(
                    "Этот пароль слишком короткий. Он должен содержать как минимум "
                    " %(min_length)d символов.",
                    "Этот пароль слишком короткий. Он должен содержать как минимум"
                    " %(min_length)d символов.",
                    self.min_length,
                ),
                code="password_too_short",
                params={"min_length": self.min_length},
            )
        

class NumericPasswordValidator(NumericPasswordValidator):

    def validate(self, password, user=None):
        if password.isdigit():
            raise ValidationError(
                _("Ваш пароль не может состоять полностью из чисел."),
                code="password_entirely_numeric",
            )
        

class CommonPasswordValidator(CommonPasswordValidator):

    def validate(self, password, user=None):
        if password.lower().strip() in self.passwords:
            raise ValidationError(
                _("Этот пароль слишком распространен."),
                code="password_too_common",
            )
       
from django.contrib.auth.password_validation import  exceeds_maximum_length_ratio, SequenceMatcher, FieldDoesNotExist, re

class UserAttributeSimilarityValidator(UserAttributeSimilarityValidator):

    def validate(self, password, user=None):
        if not user:
            return

        password = password.lower()
        for attribute_name in self.user_attributes:
            value = getattr(user, attribute_name, None)
            if not value or not isinstance(value, str):
                continue
            value_lower = value.lower()
            value_parts = re.split(r"\W+", value_lower) + [value_lower]
            for value_part in value_parts:
                if exceeds_maximum_length_ratio(
                    password, self.max_similarity, value_part
                ):
                    continue
                if (
                    SequenceMatcher(a=password, b=value_part).quick_ratio()
                    >= self.max_similarity
                ):
                    try:
                        verbose_name = str(
                            user._meta.get_field(attribute_name).verbose_name
                        )
                    except FieldDoesNotExist:
                        verbose_name = attribute_name
                    raise ValidationError(
                        _("Пароль слишком похож на имя пользователя или на почту."),
                        code="password_too_similar",
                        params={"verbose_name": verbose_name},
                    )