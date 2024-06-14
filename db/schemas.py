from pydantic import BaseModel, Field, field_validator


class Book(BaseModel):
    title: str
    author: str
    published_year: int = Field(..., gt=100, lt=2024)  #validation for year as task said
    genre: str

    @field_validator('published_year')
    def validate_published_year(cls, v):
        if not isinstance(v, int):
            raise ValueError('published_year must be an integer!!!!!!')
        if v < 1500 or v > 2023:
            raise ValueError('published_year must be between 1500 and 2023')
        return v