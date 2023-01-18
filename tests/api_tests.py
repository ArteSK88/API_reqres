import base_api

reqres = base_api.ReqRes()

# install requirements:
# pip install -r requirements.txt

# run tests:
# pytest -v tests/api_tests.py


def test_get_resource_list():
    page_num = 1
    items_per_page = 2
    status, response = reqres.get_resource_list(page_num, items_per_page)
    assert status == 200
    assert [response][0]['page'] == page_num
    assert len([response][0]['data']) == items_per_page


def test_get_user_list():
    page_num = 3
    users_per_page = 3
    status, response = reqres.get_user_list(page_num, users_per_page)
    assert status == 200
    assert [response][0]['page'] == page_num
    assert len([response][0]['data']) == users_per_page


def test_get_a_user():
    user_id = 12
    status, response = reqres.get_a_user(user_id)
    assert status == 200
    assert user_id == [response][0]['data']['id']


def test_update_a_user():
    status, response = reqres.update_a_user(1)
    assert status == 200
    assert 'updatedAt' in response


def test_patch_a_user():
    status, response = reqres.patch_a_user(1)
    assert status == 200
    assert 'updatedAt' in response


def test_delete_a_user():
    status = reqres.delete_a_user(2)
    assert status == 204


def test_get_unknown_resource():
    resource_id = 5
    status, response = reqres.get_unknown_resource(resource_id)
    assert status == 200
    assert resource_id == [response][0]['data']['id']


def test_update_unknown_resource():
    resource_id = 3
    status, response = reqres.update_unknown_resource(resource_id)
    assert status == 200
    assert 'updatedAt' in response


def test_patch_unknown_resource():
    resource_id = 5
    status, response = reqres.patch_unknown_resource(resource_id)
    assert status == 200
    assert 'updatedAt' in response


def test_delete_unknown_resource():
    status = reqres.delete_unknown_resource(1)
    assert status == 204


def test_end_session():
    status, response = reqres.end_session()
    assert status == 200


def test_create_session():
    status, response = reqres.create_session(username="iamsmallhorse", email="horse@rider.com", password="password123")
    assert status == 400
    assert "user not found" in response


def test_registrer():
    status, response = reqres.register(username="iamsmallhorse", email="horse@rider.com", password="password123")
    assert status == 400
    assert "Note: Only defined users succeed registration" in response
