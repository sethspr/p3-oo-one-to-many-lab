class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type  # runs setter
        # self._pet_type = pet_type  # does NOT run setter
        self.owner = owner  # the owner object
        Pet.all.append(self)
    
    @property
    def pet_type(self):
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self, new_pet_type):
        if new_pet_type in Pet.PET_TYPES:
            self._pet_type = new_pet_type
        else:
            raise Exception('invalid pet type')
    
    def __repr__(self):
        return f"<Pet {self.name} {self.pet_type}>"


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        # result = []
        # for pet_obj in Pet.all:
        #     if pet_obj.owner is self:
        #         result.append(pet_obj)
        # return result
        return [pet_obj for pet_obj in Pet.all if pet_obj.owner is self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception('cannot add a pet to an owner')
        pet.owner = self

    def sort_by_name(self, pet):
        return pet.name
    def get_sorted_pets(self):
        my_pets = self.pets()
        sorted_pets = sorted(my_pets, key=self.sort_by_name)
        return sorted_pets

    def __repr__(self):
        return f"<Owner {self.name}>"


# joe_obj = Owner('joe')
# fido = Pet('fido', 'dog', joe_obj)
# rex = Pet('rex', 'dog')

# joe_obj.add_pet(rex)
# print(joe_obj.pets())