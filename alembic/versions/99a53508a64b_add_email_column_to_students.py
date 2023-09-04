"""Add email column to students

Revision ID: 99a53508a64b
Revises: ea174be718e7
Create Date: 2023-09-04 18:33:08.788660

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '99a53508a64b'
down_revision: Union[str, None] = 'ea174be718e7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    
    pass
    


def downgrade() -> None:
    
    pass
