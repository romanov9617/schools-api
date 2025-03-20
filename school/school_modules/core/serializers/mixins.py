from rest_framework.exceptions import ValidationError
from rest_framework.status import HTTP_500_INTERNAL_SERVER_ERROR


class OneEntityMixin:
    def _get_serilizer_field(self):
        if hasattr(self.Meta, "short_name"):
            return self.Meta.short_name
        return self.Meta.model.__name__.lower()

    def to_internal_value(self, data):
        ser_field = self._get_serilizer_field()
        if ser_field not in data:
            raise ValidationError(
                {
                    "status": HTTP_500_INTERNAL_SERVER_ERROR,
                    "reason": f"Field {ser_field} is required",
                }
            )
        return super().to_internal_value(data[ser_field])

    def to_representation(self, instance):
        ser_field = self._get_serilizer_field()

        representation = super().to_representation(instance)
        return {ser_field: representation}
