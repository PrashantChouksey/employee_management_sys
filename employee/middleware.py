class RoleMiddleware:

    def __init__(self, get_response):
        self.get_response  = get_response
        # One time configuration and initlization

    def __call__(self, request):
        """
        code to be executed for each request before the view
        (and later middleware) are called
        :param request:
        :return:response
        """
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, *view_args, **view_kwrgs):
        """
        called just before Django calls the views return either None or Httpresponse
        :param request:
        :param view_func:
        :param view_args:
        :param view_kwrgs:
        :return:
        """
        if request.user.is_authenticated:
            request.role=None
            groups=request.user.groups.all()
            if groups:
                request.role = groups[0].name

    # def process_exception(self, request, exception):
    #     """
    #             Called for the response if exception is raised by view.
    #             return either none or HttpResponse
    #
    #     :param request:
    #     :param exception:
    #     :return:
    #     """
    # def process_template_response(self, request, response):
    #     """
    #         request = HttpRequest Object
    #         response = TemplateResonse Object
    #
    #         :return TemplateResponse use for changing template or
    #                 context if it's needed
    #
    #     :param request:
    #     :param response:
    #
    #     """
    #