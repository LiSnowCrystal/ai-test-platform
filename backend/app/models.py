from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, default="")

    # 一个项目有多个测试用例
    testcases = relationship("TestCase", back_populates="project")

class TestCase(Base):
    __tablename__ = "testcases"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    precondition = Column(String, default="")
    steps = Column(Text, default="")
    expected_result = Column(String, default="")
    project_id = Column(Integer, ForeignKey("projects.id"))

    # 这个测试用例属于哪个项目
    project = relationship("Project", back_populates="testcases")