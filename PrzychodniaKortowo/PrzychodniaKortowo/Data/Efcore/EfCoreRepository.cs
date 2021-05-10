using Microsoft.EntityFrameworkCore;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Principal;
using System.Threading.Tasks;

namespace PrzychodniaKortowo.Data.Efcore
{
    public abstract class EfCoreRepository<TEntity, Context> : IRepository<TEntity>
      where TEntity : class, IEntity
      where Context : DbContext
    {
        protected readonly Context context;
        public EfCoreRepository(Context context)
        {
            this.context = context;
        }

        public virtual async Task<TEntity> Add(TEntity entity)
        {
            context.Set<TEntity>().Add(entity);
            await context.SaveChangesAsync();
            return entity;
        }

        public virtual async Task<TEntity> Delete(int id)
        {
            var entity = await context.Set<TEntity>().FindAsync(id);
            if (entity == null)
            {
                return entity;
            }

            context.Set<TEntity>().Remove(entity);
            await context.SaveChangesAsync();

            return entity;
        }
        public virtual async Task<TEntity> DeleteById(int id, int dishId)
        {
            var entity = await context.Set<TEntity>().FindAsync(id);
            if (entity == null)
            {
                return entity;
            }

            context.Set<TEntity>().Remove(entity);
            await context.SaveChangesAsync();

            return entity;
        }
        public virtual async Task<List<TEntity>> DeleteAll(int id)
        {
            var entity = await context.Set<TEntity>().FindAsync(id);
            if (entity == null)
            {
                return entity as List<TEntity>;
            }

            context.Set<TEntity>().RemoveRange(entity);
            await context.SaveChangesAsync();

            return entity as List<TEntity>;
        }



        public virtual async Task<TEntity> Get(int id)
        {
            return await context.Set<TEntity>().FindAsync(id);
        }

        public virtual async Task<List<TEntity>> GetAll()
        {
            return await context.Set<TEntity>().ToListAsync();
        }

        public virtual async Task<TEntity> Update(TEntity entity)
        {
            context.Entry(entity).State = EntityState.Modified;
            await context.SaveChangesAsync();
            return entity;
        }
        public virtual async Task<List<TEntity>> GetAllDishesFromRestaurant(int entity)
        {
            return await context.Set<TEntity>().ToListAsync();
        }
    }
}
