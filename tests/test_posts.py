def test_get_nonexistent_post(client):
    response = client.get("/api/posts/999999?include=tags,user,comments")
    assert response.status_code == 404
    assert "detail" in response.json()


def test_get_posts_filtered(client, post_with_relations):
    response = client.get("/api/posts?status=draft&include=tags,user")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1

    post = data[0]
    assert post["status"] == "draft"
    assert "user" in post
    assert "tags" in post
    assert isinstance(post["tags"], list)
    assert len(post["tags"]) == 2


def test_get_single_post(client, post_with_relations):
    post_id = post_with_relations.id
    response = client.get(f"/api/posts/{post_id}?include=tags,user,comments")
    assert response.status_code == 200

    data = response.json()
    assert data["id"] == post_id
    assert "user" in data
    assert "tags" in data
    assert "comments" in data
    assert isinstance(data["tags"], list)
    assert isinstance(data["comments"], list)
    assert len(data["tags"]) == 2
    assert len(data["comments"]) == 1
