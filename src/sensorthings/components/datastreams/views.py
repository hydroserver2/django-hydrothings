from ninja import Query
from django.http import HttpResponse
from sensorthings import settings
from sensorthings.router import SensorThingsRouter
from sensorthings.engine import SensorThingsRequest
from sensorthings.schemas import ListQueryParams, GetQueryParams
from .schemas import DatastreamPostBody, DatastreamPatchBody, DatastreamListResponse, DatastreamGetResponse


router = SensorThingsRouter(tags=['Datastreams'])
id_qualifier = settings.ST_API_ID_QUALIFIER
id_type = settings.ST_API_ID_TYPE


@router.st_get('/Datastreams', response_schemas=(DatastreamListResponse,), url_name='list_datastream')
def list_datastreams(
        request: SensorThingsRequest,
        params: ListQueryParams = Query(...)
):
    """
    Get a collection of Datastream entities.

    <a href="http://www.opengis.net/spec/iot_sensing/1.1/req/datamodel/datastream/properties" target="_blank">\
      Datastream Properties</a> -
    <a href="http://www.opengis.net/spec/iot_sensing/1.1/req/datamodel/datastream/relations" target="_blank">\
      Datastream Relations</a>
    """

    return request.engine.list_entities(
        request=request,
        query_params=params.dict()
    )


@router.st_get(
    f'/Datastreams({id_qualifier}{{datastream_id}}{id_qualifier})',
    response_schemas=(DatastreamGetResponse,)
)
def get_datastream(
        request: SensorThingsRequest,
        datastream_id: id_type,
        params: GetQueryParams = Query(...)
):
    """
    Get a Datastream entity.

    <a href="http://www.opengis.net/spec/iot_sensing/1.1/req/datamodel/datastream/properties" target="_blank">\
      Datastream Properties</a> -
    <a href="http://www.opengis.net/spec/iot_sensing/1.1/req/datamodel/datastream/relations" target="_blank">\
      Datastream Relations</a>
    """

    return request.engine.get_entity(
        request=request,
        entity_id=datastream_id,
        query_params=params.dict()
    )


@router.st_post('/Datastreams')
def create_datastream(
        request: SensorThingsRequest,
        response: HttpResponse,
        datastream: DatastreamPostBody
):
    """
    Create a new Datastream entity.

    Links:
    <a href="http://www.opengis.net/spec/iot_sensing/1.1/req/datamodel/datastream/properties" target="_blank">\
      Datastream Properties</a> -
    <a href="http://www.opengis.net/spec/iot_sensing/1.1/req/datamodel/datastream/relations" target="_blank">\
      Datastream Relations</a> -
    <a href="http://www.opengis.net/spec/iot_sensing/1.1/req/create-update-delete/create-entity" target="_blank">\
      Create Entity</a>
    """

    return request.engine.create_entity(
        request=request,
        response=response,
        entity_body=datastream
    )


@router.patch(f'/Datastreams({id_qualifier}{{datastream_id}}{id_qualifier})')
def update_datastream(
        request: SensorThingsRequest,
        datastream_id: id_type,
        datastream: DatastreamPatchBody
):
    """
    Update an existing Datastream entity.

    Links:
    <a href="http://www.opengis.net/spec/iot_sensing/1.1/req/datamodel/datastream/properties" target="_blank">\
      Datastream Properties</a> -
    <a href="http://www.opengis.net/spec/iot_sensing/1.1/req/datamodel/datastream/relations" target="_blank">\
      Datastream Relations</a> -
    <a href="http://www.opengis.net/spec/iot_sensing/1.1/req/create-update-delete/update-entity" target="_blank">\
      Update Entity</a>
    """

    return request.engine.update_entity(
        request=request,
        entity_id=datastream_id,
        entity_body=datastream
    )


@router.delete(f'/Datastreams({id_qualifier}{{datastream_id}}{id_qualifier})')
def delete_datastream(
        request: SensorThingsRequest,
        datastream_id: id_type
):
    """
    Delete a Datastream entity.

    Links:
    <a href="http://www.opengis.net/spec/iot_sensing/1.1/req/create-update-delete/delete-entity" target="_blank">\
      Delete Entity</a>
    """

    return request.engine.delete_entity(
        request=request,
        entity_id=datastream_id
    )
