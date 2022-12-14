from RSECTION.initModel import  Model, ConvertToDlString, clearAtributes, ConvertStrToListOfInt
from RSECTION.enums import ObjectTypes

class Part():

    def __init__(self,
                 no: int = 1,
                 boundary_lines: str = None,
                 material_no: int = 1,
                 integrated_objects: bool = True,
                 integrated_objects_auto : bool = True,
                 integrated_openings: str = None,
                 comment: str = '',
                 params: dict = None,
                 model = Model):

        '''
        Args:
            no (int): Part Tag
            boundary_lines (str): Boundary Lines Number
            material_no (int): Material Number
            integrated_objects (bool): Enable/Disable Integrated Objects Option
            integrated_objects_auto (bool): Enable/Disable Integrated Objects Auto Option
            integrated_openings (str): Inegrated Openings Line Number
            comment (str, optional): Comments
            params (dict, optional): Any WS Parameter relevant to the object and its value in form of a dictionary
            model (RSECTION Class, optional): Model to be edited
        '''

        # Client model | Part
        clientObject = model.clientModel.factory.create('ns0:part')

        # Clears object atributes | Sets all atributes to None
        clearAtributes(clientObject)

        # Line No.
        clientObject.no = no

        # Boundary Lines for Part
        clientObject.boundary_lines = ConvertToDlString(boundary_lines)

        # Assigned Material

        clientObject.material = material_no

        # Integrated Objects

        if integrated_objects == True:

            if integrated_objects_auto == False:

                clientObject.auto_detection_of_integrated_objects = integrated_objects_auto
                clientObject.integrated_openings = ConvertToDlString(integrated_openings)

        else:
            clientObject.has_integrated_objects = integrated_objects

        # Comment
        clientObject.comment = comment

        if params:
            for key in params:
                clientObject[key] = params[key]

        # Add Part to client model
        model.clientModel.service.set_part(clientObject)

    @staticmethod
    def DeletePart(parts_no: str = '1 2', model = Model):

        '''
        Args:
            parts_no (str): Parts Number
            model (RSECTION Class, optional): Model to be edited
        '''

        # Delete from client model
        for part in ConvertStrToListOfInt(parts_no):
            model.clientModel.service.delete_object(ObjectTypes.E_OBJECT_TYPE_PART.name, part)

