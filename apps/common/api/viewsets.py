from rest_framework.viewsets import ReadOnlyModelViewSet


class BaseReadOnlyModelViewSet(ReadOnlyModelViewSet):

    serializer_classes = {}

    def get_serializer_class(self):
        serializer = self.serializer_classes.get(self.action)
        if serializer:
            return serializer
        return super().get_serializer_class()