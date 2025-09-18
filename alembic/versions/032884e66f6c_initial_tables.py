"""initial tables

Revision ID: 032884e66f6c
Revises: 
Create Date: 2025-04-16 15:45:13.100203

"""
from typing import Sequence, Union

from alembic import op  # type: ignore (venv)
import sqlalchemy as sa # type: ignore (venv)

# revision identifiers, used by Alembic.
revision: str = '032884e66f6c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('email', sa.String(), nullable=True),
        sa.Column('password', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)

    op.create_table('food_items',
        sa.Column('f_id', sa.Integer(), nullable=False),
        sa.Column('f_name', sa.String(), nullable=True),
        sa.Column('expiry_date', sa.DateTime(), nullable=True),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['user_id'], ['users.id']),
        sa.PrimaryKeyConstraint('f_id')
    )
    op.create_index(op.f('ix_food_items_f_id'), 'food_items', ['f_id'], unique=False)

    op.drop_table('inventory')


def downgrade() -> None:
    """Downgrade schema."""
    op.create_table('inventory',
        sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column('items', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
        sa.PrimaryKeyConstraint('user_id', name='inventory_pkey')
    )
    op.drop_index(op.f('ix_food_items_f_id'), table_name='food_items')
    op.drop_table('food_items')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')

# alembic revision --autogenerate -m "initial tables"
# alembic upgrade head