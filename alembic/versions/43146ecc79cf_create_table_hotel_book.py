"""create table hotel-book

Revision ID: 43146ecc79cf
Revises: af6e4879dec2
Create Date: 2024-11-10 10:45:16.388144

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '43146ecc79cf'
down_revision: Union[str, None] = 'af6e4879dec2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'hotel_book',
        sa.Column('hotel_id', sa.Integer()),
        sa.Column('user_id', sa.Integer()),
        sa.column('date_in', sa.String()),
        sa.Column('date_out', sa.String())
    )


def downgrade() -> None:
    op.drop_table('hotel_book')

