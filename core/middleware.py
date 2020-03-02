from users import choices as ch


class MenuAuthorizationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.menus = [
            {'privilege': ch.PRIV_VIEW_DASHBOARD, 'name': 'Dashboard', 'url_name': 'dashboard-home'},
            {'privilege': ch.PRIV_VIEW_MAP, 'name': 'Map', 'url_name': 'dashboard-map'},
            {'privilege': ch.PRIV_VIEW_PROJECTS, 'name': 'Projects', 'url_name': 'projects-home'},
            {'privilege': ch.PRIV_VIEW_SETUPS, 'name': 'Setups', 'url_name': 'setups-home'},
            {'privilege': ch.PRIV_VIEW_USERS, 'name': 'Users', 'url_name': 'users-list'},
            {'privilege': ch.PRIV_VIEW_ROLES, 'name': 'Roles', 'url_name': 'role-list'},
        ]

    def __call__(self, request):
        self.path = request.path
        if not self.path.startswith('/static') and not request.user.is_anonymous and request.user.profile.role:
            privileges = []
            for p in request.user.profile.role.privileges.all():
                privileges.append(p.privilege)
            request.allowed_menus = list(filter(lambda x: x['privilege'] in privileges, self.menus))
        else:
            request.allowed_menus = []
        response = self.get_response(request)
        return response
