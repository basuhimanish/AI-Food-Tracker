"""add phone number and food status log table

Revision ID: 7098a328b238
Revises: b169edcf5c62
Create Date: 2025-08-07 14:38:36.709077

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7098a328b238'
down_revision: Union[str, None] = 'b169edcf5c62'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Add phone_number column to users table
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    
    # Create food_status_log table
    op.create_table('food_status_log',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('inventory_id', sa.BigInteger(), nullable=True),
        sa.Column('status', sa.String(), nullable=True),
        sa.Column('timestamp', sa.DateTime(), nullable=True),
        sa.Column('quantity', sa.String(), nullable=True),
        sa.Column('notes', sa.String(), nullable=True),
        sa.ForeignKeyConstraint(['inventory_id'], ['inventory.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_food_status_log_id'), 'food_status_log', ['id'], unique=False)


def downgrade() -> None:
    """Downgrade schema."""
    # Drop food_status_log table
    op.drop_index(op.f('ix_food_status_log_id'), table_name='food_status_log')
    op.drop_table('food_status_log')
    
    # Drop phone_number column from users table
    op.drop_column('users', 'phone_number') 