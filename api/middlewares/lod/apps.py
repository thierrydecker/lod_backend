from django.apps import AppConfig


class LodConfig(AppConfig):
    name = 'lod'


class LodMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

        #
        # One-time configuration and initialization.
        #

    def __call__(self, request):
        #
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        #

        response = self.get_response(request)

        #
        # Code to be executed for each request/response after
        # the view is called
        #

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        #
        # Called just before Django calls the view.
        #
        # - request is an HttpRequest object.
        # - view_func is the Python function that Django is about to use. (It’s the actual function object, not the name
        # of the function as a string.)
        # - view_args is a list of positional arguments that will be passed to the view, and
        # - view_kwargs is a dictionary of keyword arguments that will be passed to the view.
        #
        # Neither view_args nor view_kwargs include the first view argument (request).
        #
        # If it returns None, Django will continue processing this request, executing any other process_view()
        # middleware and, then, the appropriate view
        #
        # If it returns an HttpResponse object, Django won’t bother calling the appropriate view; it’ll apply response
        # middleware to that HttpResponse and return the result.
        #
        # It should return either None or an HttpResponse object.
        #

        return None

    def process_exception(self, request, exception):
        #
        # - request is an HttpRequest object.
        # - exception is an Exception object raised by the view function.
        #
        # Django calls process_exception() when a view raises an exception. process_exception() should return either
        # None or an HttpResponse object.
        #
        # If it returns an HttpResponse object, the template response and response middleware will be applied and the
        # resulting response returned to the browser.
        #
        # Otherwise, default exception handling kicks in.
        #
        # Again, middleware are run in reverse order during the response phase, which includes process_exception.
        #
        # If an exception middleware returns a response, the process_exception methods of the middleware classes above
        # that middleware won’t be called at all.
        #

        return None

    def process_template_response(self, request, response):
        #
        # - request is an HttpRequest object.
        # - response is the TemplateResponse object (or equivalent) returned by a Django view or by a middleware.
        #
        # process_template_response() is called just after the view has finished executing, if the response instance
        # has a render() method, indicating that it is a TemplateResponse or equivalent.
        #
        # It must return a response object that implements a render method. It could alter the given response by
        # changing response.template_name and response.context_data, or it could create and return a brand-new
        # TemplateResponse or equivalent.
        #
        # You don’t need to explicitly render responses – responses will be automatically rendered once all template
        # response middleware has been called.
        #
        # Middleware are run in reverse order during the response phase, which includes process_template_response().
        #

        return response
