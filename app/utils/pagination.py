
def paginate(query, page: int, limit: int):
    offset = (page - 1) * limit
    return query.limit(limit).offset(offset)
