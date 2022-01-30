CATEGORIES_MAPPING_KEY = "categories"
ROLES_MAPPING_KEY = "roles"


def build_roles_tree(mapping):
    return {
        "categories": [
            {
                "id": f"category-{category_idx}",
                "text": mapping[CATEGORIES_MAPPING_KEY][category_idx]["name"],
                "items": [
                    {
                        "id": mapping[ROLES_MAPPING_KEY][role_id]["id"],
                        "text": mapping[ROLES_MAPPING_KEY][role_id]["name"],
                    }
                    for role_id in mapping[CATEGORIES_MAPPING_KEY][category_idx]["roleIds"]
                ]
            }
            for category_idx in mapping["categoryIdsSorted"]
        ]
    }
