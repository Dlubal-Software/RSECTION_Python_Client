from RSECTION.initModel import Model, clearAtributes, ConvertStrToListOfInt
from RSECTION.enums import ObjectTypes

class Material():

    def __init__(self,
                 no: int = 1,
                 name: str = 'Grade S275',
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Material Tag
            name (str): Material Name
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RSECTION Class, optional): Model to be edited
        '''

        # Client model | Material
        clientObject = model.clientModel.factory.create('ns0:material')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Material No.
        clientObject.no = no

        # Material Name
        clientObject.name = name

        # Comment
        clientObject.comment = comment

        # Adding optional parameters via dictionary
        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add material to client model
        model.clientModel.service.set_material(clientObject)

    @staticmethod
    def DeleteMaterial(materials_no: str = '1 2', model = Model):

        '''
        Args:
            materials_no (str): Materials Number
            model (RSECTION Class, optional): Model to be edited
        '''

        # Delete from client model
        for material in ConvertStrToListOfInt(materials_no):
            model.clientModel.service.delete_object(ObjectTypes.E_OBJECT_TYPE_MATERIAL.name, material)