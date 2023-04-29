"""Auth

Revision ID: 0b05d9ea1be5
Revises: 2fd36f192f26
Create Date: 2023-04-28 10:30:14.531502

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b05d9ea1be5'
down_revision = '2fd36f192f26'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=250), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('crated_at', sa.DateTime(), nullable=True),
    sa.Column('avatar', sa.String(length=255), nullable=True),
    sa.Column('refresh_token', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.add_column('contacts', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_unique_constraint('unique_phone_user', 'contacts', ['phone', 'user_id'])
    op.create_foreign_key(None, 'contacts', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'contacts', type_='foreignkey')
    op.drop_constraint('unique_phone_user', 'contacts', type_='unique')
    op.drop_column('contacts', 'user_id')
    op.drop_table('users')
    # ### end Alembic commands ###
