class Category:
    categories = [
        {'name': 'Category 1', 'is_published': True},
        {'name': 'Category 2', 'is_published': False},
        {'name': 'Category 3', 'is_published': True}
    ]

    @classmethod
    def add(cls, category):
        name = category.get('name')
        is_published = category.get('is_published',bool)
        if any(category['name'] == name for category in cls.categories):
            raise ValueError("Already exist!")
        else:
            new_category = {'name':name,'is_published':is_published}
            cls.categories.append(new_category)
            return new_category

    @classmethod
    def get(cls, index):
        if 0 <= index < len(cls.categories):
            return cls.categories[index]
        else:
            raise IndexError("Wrong index!")

    @classmethod
    def delete(cls, index):
        if 0 <= index < len(cls.categories):
            del cls.categories[index]

    @classmethod
    def update(cls, index, category_name):

        if 0 <= index < len(cls.categories):
            name = category_name.get('name')
            is_published = category_name.get('is_published',bool)

            if any(category['name'] == name for category in cls.categories[:index] + cls.categories[index + 1:]):
                raise ValueError("already exists!")
            else:
                cls.categories[index] = {'name': name, 'is_published': is_published}
        else:
            raise IndexError("Wrong index!")

    @classmethod
    def make_published(cls,index):
        if 0<=index<=len(cls.categories):
            cls.categories[index]['is_published'] = True
        else:
            raise IndexError("wrong index!")

    @classmethod
    def make_unpublished(cls, index):
        if 0 <= index <= len(cls.categories):
            cls.categories[index]['is_published'] = False
        else:
            raise IndexError("wrong index!")



