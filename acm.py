from typing import Dict, Set
Permissions = Dict[str, Dict[str, Set[str]]]
def load_user_acm(path: str = "data/acm_users.csv") -> Permissions:
"""Return nested dict: acm[user][resource] -> set(actions)."""
...
def check_access_user(user: str, resource: str, action: str, acm: Permissions) -> bool:
"""Return True if action is allowed for user on resource; default deny."""
