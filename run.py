import uvicorn
from main import app

if __name__ == "__main__":
    uvicorn.run(app="main:app",
                reload=True,
                port=8000,
                # workers = Скільки ядер на компьютері
                )