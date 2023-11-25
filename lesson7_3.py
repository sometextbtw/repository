class Category:
    categories = [1, 2, 3]

    @classmethod
    def add(cls, category):
        if category in cls.categories:
            raise ValueError("Already exist!")
        else:
            cls.categories.append(category)
            return cls.categories.index(category)

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
            if category_name not in cls.categories:
                cls.categories[index] = category_name
        elif index >= len(cls.categories):
            if category_name not in cls.categories:
                cls.categories.append(category_name)
        else:
            raise ValueError("not unique!")
