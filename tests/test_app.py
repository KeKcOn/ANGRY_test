import time

import pytest

from constants import STRING_FIELD_EMPTY_ERROR



@pytest.mark.asyncio
async def test_healthcheck(cli):
    resp = await cli.get('/healthcheck')
    assert resp.status == 200
    text = await resp.text()
    assert text == '{}'


@pytest.mark.asyncio
async def test_hash_success(cli):
    payload = {'string': 'test'}
    resp = await cli.post('/hash', json=payload)
    assert resp.status == 200
    response_json = await resp.json()
    assert 'hash_string' in response_json


@pytest.mark.asyncio
async def test_hash_validation_error(cli):
    payload = {}
    resp = await cli.post('/hash', json=payload)
    assert resp.status == 400
    response_json = await resp.json()
    assert 'validation_errors' in response_json
    assert response_json.get('validation_errors') == STRING_FIELD_EMPTY_ERROR
