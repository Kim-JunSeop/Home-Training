"""empty message

Revision ID: 6eca297157b5
Revises: 9ea3085d0529
Create Date: 2022-05-23 14:40:23.966991

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6eca297157b5'
down_revision = '9ea3085d0529'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('exercise__data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('exercise_type', sa.String(length=200), nullable=False),
    sa.Column('exercise_time', sa.Integer(), nullable=False),
    sa.Column('exercise_note', sa.Text(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('health__data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('height', sa.Integer(), nullable=False),
    sa.Column('weight', sa.Integer(), nullable=False),
    sa.Column('body_fat', sa.Integer(), nullable=False),
    sa.Column('body_muscle', sa.Integer(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('health_data')
    op.drop_table('exercise')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('exercise',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('exercise_type', sa.VARCHAR(length=200), nullable=False),
    sa.Column('exercise_time', sa.INTEGER(), nullable=False),
    sa.Column('exercise_note', sa.TEXT(), nullable=False),
    sa.Column('create_date', sa.DATETIME(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('health_data',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('height', sa.INTEGER(), nullable=False),
    sa.Column('weight', sa.INTEGER(), nullable=False),
    sa.Column('body_fat', sa.INTEGER(), nullable=False),
    sa.Column('body_muscle', sa.INTEGER(), nullable=False),
    sa.Column('create_date', sa.DATETIME(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('health__data')
    op.drop_table('exercise__data')
    # ### end Alembic commands ###