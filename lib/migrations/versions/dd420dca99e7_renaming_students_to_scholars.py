"""Renaming students to scholars

Revision ID: dd420dca99e7
Revises: 791279dd0760
Create Date: 2024-03-19 09:31:16.635812

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd420dca99e7'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table("students","scholars")
    pass


def downgrade() -> None:
    op.rename_table("scholars","students")
    pass
