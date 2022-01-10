from rest_framework import generics, views, viewsets, mixins
from . import log


class LoggedAPIView(views.APIView):
    @log.debug()
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


# The following definitions are not needed but
# they are presented below to illustrate how
# one can define custom View/ViewSet classes 
# to enable API logging for specific endpoints

# class LoggedGenericAPIView(generics.GenericAPIView, LoggedAPIView):
#     ...

# class LoggedViewSet(viewsets.ViewSetMixin, LoggedAPIView):
#     ...

# class LoggedGenericViewSet(viewsets.ViewSetMixin, LoggedGenericAPIView):
#     ...

# class LoggedReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet, LoggedGenericViewSet):
#     ...
    
# class LoggedModelViewSet(viewsets.ModelViewSet, LoggedGenericViewSet):
#     ...
