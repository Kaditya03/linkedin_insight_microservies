def paginate(query, page: int, limit: int):
    offset = (page - 1) * limit
    return query.offset(offset).limit(limit)
