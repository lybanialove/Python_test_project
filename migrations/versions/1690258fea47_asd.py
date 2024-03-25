"""asd

Revision ID: 1690258fea47
Revises: 400bdb02fe34
Create Date: 2024-03-15 14:53:03.851630

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1690258fea47'
down_revision: Union[str, None] = '400bdb02fe34'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
