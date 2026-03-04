def test_get_activities_returns_all_activities(client):
    response = client.get("/activities")

    payload = response.json()

    assert response.status_code == 200
    assert isinstance(payload, dict)
    assert "Chess Club" in payload


def test_get_activities_items_have_expected_shape(client):
    response = client.get("/activities")

    payload = response.json()
    first_activity = next(iter(payload.values()))

    assert response.status_code == 200
    assert "description" in first_activity
    assert "schedule" in first_activity
    assert "max_participants" in first_activity
    assert "participants" in first_activity
    assert isinstance(first_activity["participants"], list)