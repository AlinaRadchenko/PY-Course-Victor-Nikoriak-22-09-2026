from datetime import datetime, timezone
from typing import Optional

from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel, Field, field_validator

app = FastAPI(title="Notes API (FastAPI)")
NOTES: dict[int, dict] = {}


class NoteIn(BaseModel):
    title: str
    content: str = ""
    is_pinned: bool = False
    priority: int = Field(2, ge=1, le=4)

    @field_validator("title")
    @classmethod
    def title_min_length(cls, value):
        value = value.strip()
        if len(value) < 3:
            raise ValueError("Заголовок має містити щонайменше 3 символи.")
        return value


class NotePatch(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    is_pinned: Optional[bool] = None
    priority: Optional[int] = Field(None, ge=1, le=4)


@app.get("/api/notes/")
def list_notes(page: int = 1, size: int = 3):
    items = sorted(NOTES.values(), key=lambda n: (not n["is_pinned"], n["id"]))
    return {"count": len(items), "results": items[(page - 1) * size:page * size]}


@app.post("/api/notes/", status_code=201)
def create_note(body: NoteIn):
    note_id = max(NOTES, default=0) + 1
    NOTES[note_id] = {"id": note_id, **body.model_dump(), "created_at": datetime.now(timezone.utc)}
    return NOTES[note_id]


@app.get("/api/notes/{note_id}/")
def get_note(note_id: int):
    if note_id not in NOTES:
        raise HTTPException(404, "Не знайдено.")
    return NOTES[note_id]


@app.patch("/api/notes/{note_id}/")
def patch_note(note_id: int, body: NotePatch):
    note = get_note(note_id)
    note.update(body.model_dump(exclude_unset=True))
    return note


@app.delete("/api/notes/{note_id}/", status_code=204)
def delete_note(note_id: int):
    get_note(note_id)
    del NOTES[note_id]
    return Response(status_code=204)
