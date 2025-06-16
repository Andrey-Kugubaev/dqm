def test_get_user_with_posts_and_comments(client, post_with_relations):
    user_id = post_with_relations.user.id
    response = client.get(f"/api/users/{user_id}?include=posts,comments")
    assert response.status_code == 200

    data = response.json()
    assert data["id"] == user_id
    assert "posts" in data
    assert "comments" in data
    assert isinstance(data["posts"], list)
    assert isinstance(data["comments"], list)
