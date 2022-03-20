from rest_framework.fields import CharField
from rest_framework.serializers import Serializer


class CsrSerializer(Serializer):

    csr_code = CharField(allow_null=True, required=False)
    gp_id = CharField(allow_null=True, required=False)
    gp_name = CharField(allow_null=True, required=False)
    sp_id = CharField(allow_null=True, required=False)
    sp_name = CharField(allow_null=True, required=False)
    om_code = CharField(allow_null=True, required=False)
    om_name = CharField(allow_null=True, required=False)
    np_id = CharField(allow_null=True, required=False)
    np_name = CharField(allow_null=True, required=False)
    fp_id = CharField(allow_null=True, required=False)
    fp_name = CharField(allow_null=True, required=False)
