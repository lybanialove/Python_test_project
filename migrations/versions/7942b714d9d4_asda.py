"""asda

Revision ID: 7942b714d9d4
Revises: 1690258fea47
Create Date: 2024-03-18 16:57:21.201530

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7942b714d9d4'
down_revision: Union[str, None] = '1690258fea47'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
