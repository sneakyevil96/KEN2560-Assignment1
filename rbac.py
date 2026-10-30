from typing import Dict, List, Set, Optional

RolePerms = Dict[str, Dict[str, Set[str]]]
UserRoles = Dict[str, List[str]]

def load_user_roles(path: str = "data/user_roles.json") -> UserRoles:


def load_role_perms(path: str = "data/role_perms.csv") -> RolePerms:


def check_access_rbac(user: str, resource: str, action: str,
    user_roles: UserRoles, role_perms: RolePerms,
    user_allow: Optional[RolePerms] = None,
    user_deny: Optional[RolePerms] = None) -> bool:
        """Union of user roles grants allow; optional per-user allow/deny overrides (deny wins)."""