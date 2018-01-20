RENT_LIST_GET = {
    'tags': ['대여'],
    'description': '대여글 리스트 불러오기',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'category',
            'description': '볼 대여 카테고리들',
            'in': 'queryString',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': 'get 성공',
            'examples': {
                'application/json': [{
                    'id': '대여글의 id',
                    'category': '대여할 물품의 종류(카테고리)',
                    'title': '대여 글의 제목',
                    'photo': '대여 글에 들어갈 사진'
                },
                    {
                    'id': '대여글의 id',
                    'category': '대여할 물품의 종류(카테고리)',
                    'title': '대여 글의 제목',
                    'photo': '대여 글에 들어가는 사진'
                }
                ]
            }
        },
        '204': {
            'description': '글 없음'
        }
    }
}

RENT_GET = {
    'tags': ['대여'],
    'description': '대여글 읽기',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'id',
            'description': '볼 대여글의 id',
            'in': 'queryString',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '200': {
            'description': 'get 성공',
            'examples': {
                'application/json': {
                    'id': '게시글의 id',
                    'category': '대여할 물품의 종류(카테고리)',
                    'title': '대여 글의 제목',
                    'author_id': '글 작성자의 id',
                    'author_nickname': '글 작성자의 닉네임',
                    'hour_price': '시간당 가격',
                    'day_price': '하루당 가격',
                    'photo': '대여 글에 들어가는 사진'
                }
            }
        },
        '204': {
            'description': '글 없음'
        }
    }
}

RENT_POST = {
    'tags': ['대여'],
    'description': '대여글 쓰기',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'category',
            'description': '작성할 글의 카테고리',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'hour_price',
            'description': '시간당 가격',
            'in': 'json',
            'type': 'int',
            'required': False
        },
        {
            'name': 'day_price',
            'description': '하루당 가격',
            'in': 'json',
            'type': 'int',
            'required': False
        },
        {
            'name': 'title',
            'description': '글의 제목',
            'in': 'json',
            'type': 'str',
            'required': True
        },
        {
            'name': 'content',
            'description': '글의 내용',
            'in': 'json',
            'type': 'str',
            'required': True
        },
    ],
    'responses': {
        '201': {
            'description': '글 작성 성공'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}

RENT_DELETE = {
    'tags': ['대여'],
    'description': '대여 글 삭제',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str',
            'required': True
        },
        {
            'name': 'id',
            'description': '삭제할 대여글의 id',
            'in': 'formData',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '글 삭제 성공'
        },
        '403': {
            'description': '권한 없음'
        }
    }
}