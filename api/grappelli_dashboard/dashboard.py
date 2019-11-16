from django.utils.translation import ugettext_lazy as _
from grappelli.dashboard import Dashboard, modules
from grappelli.dashboard.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):
    """
    Custom dashboard for LOD
    """

    def init_with_context(self, context):
        site_name = get_admin_site_name(context)

        #
        # LOD
        #
        self.children.append(modules.ModelList(
                title='All Models',
                column=1,
                collapsible=True,
        ))

        # append a recent actions module
        self.children.append(modules.RecentActions(
                _('Recent Actions'),
                limit=5,
                collapsible=True,
                column=3,
        ))
